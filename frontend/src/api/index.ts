import axios from 'axios'
import type { Referral, CreateReferralRequest, ReferralAnalytics, PaginatedResponse } from './../types'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
})

export const fetchReferrals = async (page: number = 1): Promise<PaginatedResponse<Referral>> =>
  api.get('/referrals/', { params: { page } }).then((response) => response.data)

export const createReferral = async (payload: CreateReferralRequest): Promise<Referral> =>
  api.post('/referrals/', payload).then((response) => response.data)

export const resendReferral = (id: number): Promise<Referral> =>
  api.post(`/referrals/${id}/resend/`).then((response) => response.data)

export const lookupByToken = (token: string): Promise<Referral> =>
  api.get('/referrals/lookup/', { params: { token } }).then(res => res.data)

export const fetchAnalytics = (): Promise<ReferralAnalytics> =>
  api.get('/referrals/analytics/').then((response) => response.data)