<script setup lang="ts">
import StatusPill from './StatusPill.vue'

const referrals = [
  { id: 1, name: 'Sarah Johnson',    email: 'sarah@example.com',   status: 'joined',                date: 'Nov 15, 2024', joinedOn: 'Dec 2, 2024' },
  { id: 2, name: 'Michael Chen',     email: 'michael@example.com', status: 'application_received',  date: 'Dec 1, 2024',  joinedOn: null },
  { id: 3, name: 'Jessica Rodriguez',email: 'jessica@example.com', status: 'invitation_sent',       date: 'Dec 8, 2024',  joinedOn: null },
  { id: 4, name: 'David Kim',        email: 'david@example.com',   status: 'joined',                date: 'Oct 22, 2024', joinedOn: 'Nov 10, 2024' },
]
</script>

<template>
  <div class="bg-dark-card border border-dark-border rounded-2xl p-6">
    <h2 class="text-xl font-serif text-gray-primary mb-1">Your Member Referrals</h2>
    <p class="text-sm text-gray-secondary mb-6">Track the status of your referrals and see when they join.</p>

    <!-- Empty state -->
    <div v-if="referrals.length === 0" class="text-center py-12 text-gray-tertiary">
      <p class="text-sm">No referrals yet. Invite someone to get started.</p>
    </div>

    <!-- Table -->
    <div v-else class="overflow-x-auto">
      <table class="w-full text-sm">
        <thead>
          <tr class="text-gray-tertiary text-left border-b border-dark-border">
            <th class="pb-3 font-medium pr-6">Name</th>
            <th class="pb-3 font-medium pr-6">Email</th>
            <th class="pb-3 font-medium pr-6">Status</th>
            <th class="pb-3 font-medium pr-6">Invited Date</th>
            <th class="pb-3 font-medium"></th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="referral in referrals"
            :key="referral.id"
            class="border-b border-dark-border last:border-0"
          >
            <td class="py-4 pr-6 font-semibold text-gray-primary">{{ referral.name }}</td>
            <td class="py-4 pr-6 text-gray-secondary">{{ referral.email }}</td>
            <td class="py-4 pr-6">
              <StatusPill :status="referral.status as any" :date="referral.joinedOn ?? undefined" />
            </td>
            <td class="py-4 pr-6 text-gray-secondary">
              <span class="inline-flex items-center gap-1.5">
                <!-- calendar icon -->
                <svg class="w-3.5 h-3.5 text-gray-tertiary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>
                </svg>
                {{ referral.date }}
              </span>
            </td>
            <td class="py-4 text-right">
              <button
                v-if="referral.status === 'invitation_sent'"
                class="inline-flex items-center gap-1.5 text-gray-secondary hover:text-gray-primary transition-colors text-sm"
              >
                Re-send
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
                </svg>
              </button>
              <span v-else class="text-gray-tertiary text-sm">N/A</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
