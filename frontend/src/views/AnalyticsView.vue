<script setup lang="ts">
import { onMounted, computed } from 'vue'
import { Doughnut } from 'vue-chartjs'
import { Chart as ChartJS, ArcElement, Tooltip } from 'chart.js'
import { useReferralStore } from '../stores/referral'
import StatCard from '../components/StatCard.vue'

ChartJS.register(ArcElement, Tooltip)

const store = useReferralStore()

onMounted(() => store.getAnalytics())

const chartData = computed(() => ({
  labels: ['Joined', 'Not Converted'],
  datasets: [
    {
      data: [
        store.analytics?.conversion_rate ?? 0,
        100 - (store.analytics?.conversion_rate ?? 0),
      ],
      backgroundColor: ['#10B981', '#374151'],
      borderColor: ['#10B981', '#374151'],
      borderWidth: 1,
    },
  ],
}))

const chartOptions = {
  responsive: true,
  cutout: '75%',
  plugins: {
    legend: { display: false },
    tooltip: { enabled: false },
  },
}
</script>

<template>
  <div>
    <h1 class="text-4xl font-serif text-gray-primary mb-2">Analytics</h1>
    <p class="text-gray-secondary mb-8">Overview of your referral program performance.</p>

    <!-- Loading -->
    <div v-if="store.loadingAnalytics" class="text-center py-12 text-gray-tertiary">
      <p class="text-sm">Loading analytics...</p>
    </div>

    <!-- Error -->
    <div v-else-if="store.analyticsError" class="text-center py-12 text-red-400">
      <p class="text-sm">{{ store.analyticsError }}</p>
    </div>

    <template v-else-if="store.analytics">
      <!-- Stat cards -->
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6">
        <StatCard label="Total Invited" :value="store.analytics.total_invited" />
        <StatCard label="Invitations Sent" :value="store.analytics.invitations_sent" />
        <StatCard label="Joined" :value="store.analytics.joined" />
      </div>

      <!-- Conversion rate doughnut -->
      <div class="bg-dark-card border border-dark-border rounded-2xl p-6 flex flex-col items-center">
        <h2 class="text-xl font-serif text-gray-primary mb-6 self-start">Conversion Rate</h2>
        <div class="relative w-48 h-48">
          <Doughnut :data="chartData" :options="chartOptions" />
          <div class="absolute inset-0 flex items-center justify-center pointer-events-none">
            <span class="text-3xl font-serif text-gray-primary">
              {{ store.analytics.conversion_rate }}%
            </span>
          </div>
        </div>
        <div class="flex items-center gap-6 mt-6 text-sm text-gray-secondary">
          <span class="inline-flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-success inline-block"></span>
            Joined
          </span>
          <span class="inline-flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-dark-border inline-block"></span>
            Not Converted
          </span>
        </div>
      </div>
    </template>
  </div>
</template>
