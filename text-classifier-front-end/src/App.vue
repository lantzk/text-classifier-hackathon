<script lang="ts" setup>
  import { useRouter } from 'vue-router'

  const router = useRouter()

  const goTo = (destination: string) => {
    router.push({ path: destination })
  }
</script>

<template>
  <v-app>
    <v-main>
      <v-app-bar :elevation="2">
        <v-app-bar-title>
          <v-btn
            @click="goTo('/')"
          >Content Classifier</v-btn>
        </v-app-bar-title>
      </v-app-bar>
      <v-container>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>
