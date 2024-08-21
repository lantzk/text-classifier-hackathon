<script setup lang="ts">
  import { useAppStore } from '../stores/app'
  const store = useAppStore()


</script>

<template>
  <v-row>
    <v-col>
      <v-row>
        <v-col>
          <h2
            class="mt-4"
          >Your Analysis</h2>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <p>{{ store.getResults }}</p>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
