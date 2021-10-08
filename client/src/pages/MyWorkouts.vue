<template>
  <div id="my_workouts">
    <div
      class="workout_card"
      v-for="workout in workouts.data"
      :key="workout.id"
    >
      <p>{{ workout.duration }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'MyWorkouts',
  conponents: {},
  data: () => ({
    workouts: null
  }),
  mounted: async function () {
    await this.getAllWorkouts()
  },
  methods: {
    async getAllWorkouts() {
      const res = await axios.get('http://localhost:5000/comments')
      this.workouts = res
    }
  }
}
</script>

<style scoped>
</style>