import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { CreateReferralRequest, Referral, ReferralAnalytics } from '../types'
import axios from 'axios'
import { createReferral, fetchAnalytics, fetchReferrals, resendReferral as resendReferralApi } from '../api'

export const useReferralStore = defineStore('referral', () => {
  const referrals = ref<Referral[]>([])
  const analytics = ref<ReferralAnalytics | null>(null)
  const error = ref<string | null>(null)
  const resendError = ref<string | null>(null)

  const loadingFetch = ref(false)
  const loadingCreate = ref(false)
  const loadingResend = ref<number | null>(null)
  const loadingAnalytics = ref(false)

  const extractError = (err: unknown): string => {
    if (axios.isAxiosError(err)) {
      return err.response?.data?.detail ?? 'An unexpected error occurred.'
    }

    return 'An unexpected error occurred.'
  }

  const getReferrals = async (): Promise<void> => {
    loadingFetch.value = true
    error.value = null

    try {
      referrals.value = await fetchReferrals() // TODO: send page number
    } catch (err) {
      error.value = extractError(err)
    } finally {
      loadingFetch.value = false
    }
  }

  const addReferral = async (payload: CreateReferralRequest): Promise<boolean>  => {
    loadingCreate.value = true
    error.value = null

    try {
      const referral = await createReferral(payload)
      referrals.value.unshift(referral)
      return true
    } catch (err) {
      error.value = extractError(err)
      return false
    } finally {
      loadingCreate.value = false
    }
  }

  const resendReferral = async (id: number): Promise<void> => {
    loadingResend.value = id
    resendError.value = null

    try {
      const updated = await resendReferralApi(id)
      const index = referrals.value.findIndex(r => r.id === id)

      if (index !== -1) {
        referrals.value[index] = updated
      }
    } catch (err) {
      resendError.value = extractError(err)
    } finally {
      loadingResend.value = null
    }
  }

  const getAnalytics = async (): Promise<void> => {
    loadingAnalytics.value = true
    error.value = null

    try {
      analytics.value = await fetchAnalytics()
    } catch (err) {
      error.value = extractError(err)
    } finally {
      loadingAnalytics.value = false
    }
  }

  return {
    referrals,
    analytics,
    error,
    resendError,
    loadingFetch,
    loadingCreate,
    loadingResend,
    loadingAnalytics,
    getReferrals,
    addReferral,
    resendReferral,
    getAnalytics,
  }
})