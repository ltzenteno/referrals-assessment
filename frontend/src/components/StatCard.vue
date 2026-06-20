<script setup lang="ts">
defineProps<{
  label: string
  value: number | string
}>()
</script>

<template>
  <div class="bg-dark-card border border-dark-border rounded-2xl p-6">
    <p class="text-sm text-gray-secondary mb-2">{{ label }}</p>
    <p class="text-4xl font-serif text-gray-primary">{{ value }}</p>
  </div>
</template>
