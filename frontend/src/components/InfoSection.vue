<template>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
    <!-- Why Invite? -->
    <div class="bg-dark-card border border-dark-border rounded-2xl p-6">
      <h3 class="text-lg font-serif text-copper flex items-center gap-2 mb-3">
        <!-- people icon -->
        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>
          <path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>
        </svg>
        Why Invite?
      </h3>
      <p class="text-sm text-gray-secondary leading-relaxed">
        By inviting someone, you're expediting their access to 10 East's curated
        co-investment opportunities and investor network.
      </p>
    </div>

    <!-- How it Works -->
    <div class="bg-dark-card border border-dark-border rounded-2xl p-6">
      <h3 class="text-lg font-serif text-copper flex items-center gap-2 mb-3">
        <!-- question/info icon -->
        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>
        </svg>
        How it Works
      </h3>
      <ol class="text-sm text-gray-secondary space-y-2 leading-relaxed list-none">
        <li class="flex gap-2"><span class="text-gray-tertiary shrink-0">1.</span> Fill in the referral form with their name and email.</li>
        <li class="flex gap-2"><span class="text-gray-tertiary shrink-0">2.</span> We'll send them an email invitation to apply for 10 East membership.</li>
        <li class="flex gap-2"><span class="text-gray-tertiary shrink-0">3.</span> Your referral can explore and decide if 10 East is the right fit for them.</li>
      </ol>
    </div>
  </div>
</template>
