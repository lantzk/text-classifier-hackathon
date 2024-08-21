// Utilities
import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
  state: () => {
    return {
      results: null,
    }
  },
  getters: {
    getResults(): any {
      return this.results
    }
  },
  actions: {
    setResults(data: any) {
      this.results = data
    }
  },
})
