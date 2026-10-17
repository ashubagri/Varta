# VARTA Content Moderation

VARTA is an early-stage community prototype. Members can report posts, replies, and profiles for review.

## Report reasons

- Spam
- Harassment or hate
- Threats or violence
- Misinformation
- Sexual content
- Privacy violation
- Other

A member can submit one report per target. Reports are private: members can only read their own reports, and reports cannot be edited or deleted by ordinary members.

## Review reports as the project owner

Open the [VARTA Moderation Dashboard](https://ashubagri.github.io/Varta/moderation.html) while signed in with an authorized moderator account. It lists reports, shows the reported content when it is still available, and lets moderators change report status. The dashboard is not indexed by search engines, but its security comes from Supabase authentication and moderator-role policies, not from the URL being secret.

If you need direct database review, open the VARTA Supabase project and use the SQL Editor while signed in as the project owner. Review open reports with:

```sql
select
  id,
  created_at,
  reporter_id,
  target_type,
  target_id,
  reason,
  details,
  status
from public.content_reports
where status = 'open'
order by created_at asc;
```

To mark a report as under review:

```sql
update public.content_reports
set status = 'reviewing'
where id = 'REPORT_UUID_HERE';
```

After reviewing the reported content, record the outcome:

```sql
update public.content_reports
set status = 'resolved'
where id = 'REPORT_UUID_HERE';
```

Use `dismissed` instead of `resolved` when no action is warranted. Replace `REPORT_UUID_HERE` with the actual report ID. Do not expose reporter details publicly.

## Important limitations

- Reports are not automatically proof of a violation; review context before acting.
- The prototype does not yet have an in-site moderator dashboard, automatic content removal, or member-blocking feature.
- Report records store target IDs and reason/details; they do not take a snapshot of the reported content. If content is edited or removed, review available context before deciding.
- Keep review actions restricted to trusted project administrators. Do not grant ordinary members permission to update report status.
- Publish clear community standards and a contact route before opening VARTA to a larger public audience.


## Review knowledge contributions

Open the [VARTA Editorial Review Queue](https://ashubagri.github.io/Varta/editorial.html) while signed in with an authorized moderator account. Review member suggestions, select a decision, and optionally leave a note for the contributor. Accepted suggestions are not automatically published; editorial content must still be prepared and added to the relevant knowledge page deliberately. Access is enforced by Supabase authentication and moderator-role policies.
