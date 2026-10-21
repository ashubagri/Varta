create or replace function public.varta_moderate_video_before_write()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  -- Keep uploads private until the authenticated Edge Function finishes moderation.
  new.status := 'pending';
  new.moderation_reason := null;
  new.reviewed_at := null;
  new.reviewed_by := null;
  return new;
end;
$$;
