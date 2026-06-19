<script setup lang="ts">
defineProps<{
  status: 'invitation_sent' | 'application_received' | 'joined' | 'declined'
  date?: string
}>()

const config = {
  invitation_sent: {
    label: 'Invitation Sent',
    classes: 'bg-gray-700 text-gray-300',
    icon: 'mail',
  },
  application_received: {
    label: 'Application Received',
    classes: 'bg-blue-900/50 text-blue-300',
    icon: 'clock',
  },
  joined: {
    label: 'Joined',
    classes: 'bg-success/20 text-success',
    icon: 'check',
  },
  declined: {
    label: 'Declined',
    classes: 'bg-red-900/50 text-red-400',
    icon: 'x',
  },
}
</script>

<template>
  <span
    :class="config[status].classes"
    class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium whitespace-nowrap"
  >
    <!-- mail icon -->
    <svg v-if="config[status].icon === 'mail'" class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
    </svg>
    <!-- clock icon -->
    <svg v-else-if="config[status].icon === 'clock'" class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
    </svg>
    <!-- check icon -->
    <svg v-else-if="config[status].icon === 'check'" class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M20 6 9 17l-5-5"/>
    </svg>
    <!-- x icon -->
    <svg v-else-if="config[status].icon === 'x'" class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M18 6 6 18M6 6l12 12"/>
    </svg>

    {{ status === 'joined' && date ? `Joined on ${date}` : config[status].label }}
  </span>
</template>
