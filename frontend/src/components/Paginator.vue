<script setup lang="ts">
defineProps<{
  currentPage: number
  totalPages: number
}>()

defineEmits<{
  prev: []
  next: []
}>()
</script>

<template>
  <div v-if="totalPages > 1" class="flex items-center justify-end gap-3 mt-4 pt-4 border-t border-dark-border">
    <button
      @click="$emit('prev')"
      :disabled="currentPage === 1"
      class="p-1.5 rounded-lg text-gray-secondary hover:text-gray-primary disabled:opacity-30 disabled:cursor-not-allowed transition-colors"
    >
      <!-- caret left -->
      <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M15 18l-6-6 6-6"/>
      </svg>
    </button>

    <span class="text-sm text-gray-secondary">
      Page <span class="text-gray-primary font-medium">{{ currentPage }}</span> of
      <span class="text-gray-primary font-medium">{{ totalPages }}</span>
    </span>

    <button
      @click="$emit('next')"
      :disabled="currentPage === totalPages"
      class="p-1.5 rounded-lg text-gray-secondary hover:text-gray-primary disabled:opacity-30 disabled:cursor-not-allowed transition-colors"
    >
      <!-- caret right -->
      <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M9 18l6-6-6-6"/>
      </svg>
    </button>
  </div>
</template>