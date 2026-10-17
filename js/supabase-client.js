
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2';

const SUPABASE_URL = 'https://vwjugxvxlgatskmijkqg.supabase.co';
const SUPABASE_PUBLISHABLE_KEY = 'sb_publishable_5l2FG9CoXzAy06ynkfN-wA_V0o0sx3o';

export const supabase = createClient(
  SUPABASE_URL,
  SUPABASE_PUBLISHABLE_KEY
);
