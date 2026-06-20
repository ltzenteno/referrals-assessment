<script setup lang="ts">
import InviteForm from '../components/InviteForm.vue'
import ReferralTable from '../components/ReferralTable.vue'
import InfoSection from '../components/InfoSection.vue'
</script>

<template>
  <div>
    <h1 class="text-4xl font-serif text-gray-primary mb-2">Invite a Member</h1>
    <p class="text-gray-secondary mb-8">
      Help grow our community by referring qualified investors. We expect all members to uphold our
      <a href="#" class="underline text-gray-primary">Code of Standards</a>.
    </p>
    <div class="space-y-6">
      <InviteForm />
      <ReferralTable />
      <InfoSection />
    </div>
  </div>
</template>
