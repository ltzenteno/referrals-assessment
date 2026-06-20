<script setup lang="ts">
import { RouterView, RouterLink } from 'vue-router'
</script>

<template>
  <div class="min-h-screen bg-dark-bg">
    <!-- Nav -->
    <nav class="border-b border-dark-border">
      <div class="container mx-auto px-4 max-w-5xl h-14 flex items-center justify-between">
        <span class="font-serif text-gray-primary text-lg">10 East</span>
        <div class="flex items-center gap-6 text-sm">
          <RouterLink
            to="/"
            class="text-gray-secondary hover:text-gray-primary transition-colors"
            active-class="text-gray-primary font-medium"
          >
            Referrals
          </RouterLink>
          <RouterLink
            to="/analytics"
            class="text-gray-secondary hover:text-gray-primary transition-colors"
            active-class="text-gray-primary font-medium"
          >
            Analytics
          </RouterLink>
        </div>
      </div>
    </nav>

    <!-- Page content -->
    <div class="container mx-auto px-4 py-10 max-w-5xl">
      <RouterView />
    </div>
  </div>
</template>
