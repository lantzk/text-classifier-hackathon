<script setup lang="ts">
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
      <v-row>
        <v-col>
          <v-textarea
            class="mt-4"
            clear-icon="mdi-close-circle"
            clearable
            label="Content"
            model-value=""
          ></v-textarea>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-btn
            color="primary"
            block
          >Analyze It</v-btn>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
