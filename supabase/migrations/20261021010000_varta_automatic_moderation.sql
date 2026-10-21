-- VARTA automatic text moderation without an external AI API.
create or replace function public.varta_moderation_result(p_text text)
returns text
language plpgsql
immutable
set search_path = ''
as $$
declare
  t text := lower(coalesce(p_text, ''));
begin
  if t ~* '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}' then
    return 'rejected: exposed email address';
  end if;
  if t ~ '(^|[^0-9])(\+?91[[:space:]-]?)?[6-9][0-9]{9}([^0-9]|$)' then
    return 'rejected: possible personal phone number';
  end if;
  if (length(t) - length(replace(t, 'http://', ''))) / 7
     + (length(t) - length(replace(t, 'https://', ''))) / 8 > 4 then
    return 'rejected: excessive links';
  end if;
  if t ~* '(claim your prize|you have won|double your money|send bitcoin to|buy followers|free followers|guaranteed daily income|earn money fast|limited time crypto giveaway)' then
    return 'rejected: likely promotional spam';
  end if;
  return 'published';
end;
$$;

create or replace function public.varta_moderate_video_before_write()
returns trigger
language plpgsql
set search_path = ''
as $$
declare
  result text;
begin
  result := public.varta_moderation_result(coalesce(new.title, '') || E'\n' || coalesce(new.description, ''));
  new.moderation_reason := null;
  new.reviewed_at := null;
  new.reviewed_by := null;
  if result <> 'published' then
    new.status := 'rejected';
    new.moderation_reason := result;
  else
    new.status := 'published';
  end if;
  return new;
end;
$$;

alter table public.video_posts
  add column if not exists moderation_reason text;

drop trigger if exists varta_auto_moderate_video on public.video_posts;
create trigger varta_auto_moderate_video
before insert on public.video_posts
for each row execute function public.varta_moderate_video_before_write();

drop policy if exists "Members can submit their own pending videos" on public.video_posts;
create policy "Members can submit videos for automatic moderation"
on public.video_posts for insert to authenticated
with check (user_id = (select auth.uid()) and object_path like (select auth.uid())::text || '/%');

create or replace function public.varta_reject_flagged_text()
returns trigger
language plpgsql
set search_path = ''
as $$
declare
  result text;
begin
  result := public.varta_moderation_result(new.content);
  if result <> 'published' then
    raise exception 'VARTA automatic moderation blocked this submission: %', result
      using errcode = 'check_violation';
  end if;
  return new;
end;
$$;

drop trigger if exists varta_auto_moderate_post on public.posts;
create trigger varta_auto_moderate_post
before insert on public.posts
for each row execute function public.varta_reject_flagged_text();

drop trigger if exists varta_auto_moderate_reply on public.replies;
create trigger varta_auto_moderate_reply
before insert on public.replies
for each row execute function public.varta_reject_flagged_text();

update public.video_posts
set status = case
      when public.varta_moderation_result(coalesce(title, '') || E'\n' || coalesce(description, '')) = 'published' then 'published'
      else 'rejected'
    end,
    moderation_reason = case
      when public.varta_moderation_result(coalesce(title, '') || E'\n' || coalesce(description, '')) = 'published' then null
      else public.varta_moderation_result(coalesce(title, '') || E'\n' || coalesce(description, ''))
    end,
    reviewed_at = null,
    reviewed_by = null
where status = 'pending';
