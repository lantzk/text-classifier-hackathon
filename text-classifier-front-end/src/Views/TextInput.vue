<script setup lang="ts">
  import { ref, type Ref } from 'vue'
  import axios from 'axios'
  import { useAppStore } from '../stores/app'
  import { useRouter } from 'vue-router'

  const router = useRouter()

  const loading: Ref<boolean> = ref(false)
  const errors: Ref<string[]> = ref([])
  const content: Ref<string> = ref('')
  const store = useAppStore()

  const analyzeText = async () => {
    loading.value = true
    errors.value = []

    try {
      const result = await axios.post(
        'http://localhost:8000/classify',
        {
          text: content.value,
        },
        {}
      )

      store.setResults(result.data)
      await router.push({ path: '/output' })

      loading.value = false
    } catch (error) {
      console.log(error)
      loading.value = false
      errors.value.push('There was an error while analyzing your file, try again.')
    }
  }
</script>

<template>
  <v-row>
    <v-col>
      <v-row>
        <v-col>
          <h2
            class="mt-4"
          >Paste Your Content Here</h2>
        </v-col>
      </v-row>
      <v-row
        v-if="errors.length > 0"
      >
        <v-col>
          <v-alert
            border
            density="compact"
            title="Error"
            type="error"
          >
            <ul>
              <li v-for="(error, i) in errors" :key="i">
                {{ error }}
              </li>
            </ul>
          </v-alert>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-textarea
            v-model="content"
            class="mt-4"
            clear-icon="mdi-close-circle"
            clearable
            label="Content"
          />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-btn
            block
            color="primary"
            @click="analyzeText"
          >Analyze It</v-btn>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
