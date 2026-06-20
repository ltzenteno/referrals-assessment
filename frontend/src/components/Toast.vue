<script setup lang="ts">
import { watch, onUnmounted } from 'vue'

const props = defineProps<{
  message: string | null
  type?: 'error' | 'success'
}>()

const emit = defineEmits<{
  close: []
}>()

let timer: ReturnType<typeof setTimeout> | null = null

watch(() => props.message, (val) => {
  if (timer) {
    clearTimeout(timer)
  }

  if (val) {
    timer = setTimeout(() => emit('close'), 2000)
  }
}, { immediate: true })

onUnmounted(() => {
  if (timer) {
    clearTimeout(timer)
  }
})
</script>

<template>
  <Transition
    enter-active-class="transition duration-300 ease-out"
    enter-from-class="opacity-0 translate-x-4"
    enter-to-class="opacity-100 translate-x-0"
    leave-active-class="transition duration-200 ease-in"
    leave-from-class="opacity-100 translate-x-0"
    leave-to-class="opacity-0 translate-x-4"
  >
    <div
      v-if="message"
      :class="type === 'success'
        ? 'border-green-800'
        : 'border-red-800'"
      class="fixed top-6 right-6 z-50 flex items-start gap-3 bg-dark-card border rounded-xl px-4 py-3 shadow-lg max-w-sm"
    >
      <!-- success icon -->
      <svg v-if="type === 'success'" class="w-4 h-4 text-success shrink-0 mt-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"/><path d="M9 12l2 2 4-4"/>
      </svg>
      <!-- error icon -->
      <svg v-else class="w-4 h-4 text-red-400 shrink-0 mt-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"/><path d="M12 8v4m0 4h.01"/>
      </svg>

      <p :class="type === 'success' ? 'text-success' : 'text-red-400'" class="text-sm flex-1">{{ message }}</p>

      <!-- close button -->
      <button
        @click="emit('close')"
        class="text-gray-tertiary hover:text-gray-primary transition-colors shrink-0"
      >
        <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M18 6 6 18M6 6l12 12"/>
        </svg>
      </button>
    </div>
  </Transition>
</template>