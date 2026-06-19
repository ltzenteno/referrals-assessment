<script setup lang="ts">
import { ref, computed } from 'vue'
import { useReferralStore } from '../stores/referral'

const store = useReferralStore()

const name = ref('')
const email = ref('')
const fieldError = ref<string | null>(null)

const isSubmitEnabled = computed(() =>
  name.value.trim().length > 0 &&
  email.value.trim().length > 0 &&
  !store.loadingCreate
)

const handleSubmit = async (): Promise<void> => {
  fieldError.value = null

  // splitting the name into first and last name (simple approach)
  const parts = name.value.trim().split(' ')
  if (parts.length < 2 || !parts[1]) {
    fieldError.value = 'Please enter the full name (first and last).'
    return
  }

  const firstName = parts[0]
  const lastName = parts.slice(1).join(' ')

  const success = await store.addReferral({
    first_name: firstName,
    last_name: lastName,
    email: email.value.trim(),
  })

  if (success) {
    // Clear the form on success
    name.value = ''
    email.value = ''
    fieldError.value = null
  } else {
    fieldError.value = store.error || 'An error occurred while sending the invitation.'
  }
}

</script>

<template>
  <div class="bg-dark-card border border-dark-border rounded-2xl p-6">
    <form @submit.prevent="handleSubmit">
      <div class="flex flex-col md:flex-row md:items-end gap-4">
        <!-- Name field -->
        <div class="flex-1">
          <label class="block text-sm font-semibold text-gray-primary mb-1">
            Invitee's Name*
          </label>
          <input
            v-model="name"
            type="text"
            placeholder="Enter their full name"
            class="w-full bg-dark-bg border border-dark-border rounded-lg px-4 py-2.5 text-gray-primary placeholder-gray-tertiary focus:outline-none focus:border-copper"
          />
        </div>

        <!-- Email field -->
        <div class="flex-1">
          <label class="block text-sm font-semibold text-gray-primary mb-1">
            Invitee's Email*
          </label>
          <input
            v-model="email"
            type="email"
            placeholder="Enter their email address"
            class="w-full bg-dark-bg border border-dark-border rounded-lg px-4 py-2.5 text-gray-primary placeholder-gray-tertiary focus:outline-none focus:border-copper"
          />
        </div>

        <!-- Submit button -->
        <button
          type="submit"
          :disabled="!isSubmitEnabled"
          class="bg-copper hover:bg-copper-dark disabled:opacity-50 disabled:cursor-not-allowed text-white font-semibold px-6 py-2.5 rounded-lg transition-colors whitespace-nowrap"
        >
          {{ store.loadingCreate ? 'Sending...' : 'Send Invitation' }}
        </button>
      </div>

      <!-- Inline error -->
      <p v-if="fieldError" class="mt-3 text-sm text-red-400">{{ fieldError }}</p>

      <!-- Privacy notice -->
      <div class="flex items-center gap-3 mt-5 pt-5 border-t border-dark-border">
        <div class="flex items-center justify-center w-8 h-8 rounded-full bg-success/20 text-success shrink-0">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
          </svg>
        </div>
        <p class="text-sm text-gray-secondary">
          <span class="font-bold text-gray-primary">We take privacy seriously:</span>
          Your referral's information will be handled with the utmost care and confidentiality.
        </p>
      </div>
    </form>
  </div>
</template>
