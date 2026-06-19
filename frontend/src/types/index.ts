export type ReferralStatus = 'invitation_sent' | 'application_received' | 'joined' | 'declined'

export interface Referral {
  id: number
  first_name: string
  last_name: string
  email: string
  status: ReferralStatus
  created_at: string
  last_sent_at: string | null
}

export type CreateReferralRequest = Pick<Referral, 'first_name' | 'last_name' | 'email'>

export interface ReferralAnalytics {
  total_invited: number
  invitations_sent: number
  joined: number
  conversion_rate: number
}

export interface ApiError {
  detail: string
}

export interface PaginatedResponse<T> {
  count: number
  next: string | null
  previous: string | null
  results: T[]
}
