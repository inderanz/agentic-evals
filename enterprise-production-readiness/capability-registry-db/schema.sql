create table capabilities (
  id text primary key,
  name text not null,
  type text not null check (type in ('skill','mcp-server','agent','prompt-package','workflow')),
  owner text not null,
  support_channel text not null,
  created_at timestamptz not null default now()
);

create table capability_versions (
  id bigserial primary key,
  capability_id text not null references capabilities(id),
  version text not null,
  repository_url text not null,
  commit_sha text not null,
  risk_level text not null,
  data_classification text not null,
  score integer not null,
  status text not null check (status in ('certified','rejected','expired','deprecated')),
  scorecard_uri text,
  evidence_uri text,
  certified_at timestamptz,
  expires_at timestamptz,
  unique(capability_id, version)
);

create table approvals (
  id bigserial primary key,
  capability_version_id bigint not null references capability_versions(id),
  approver text not null,
  approval_type text not null,
  decision text not null check (decision in ('approved','rejected','exception')),
  comment text,
  created_at timestamptz not null default now()
);
