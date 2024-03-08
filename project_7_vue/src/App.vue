<template>
  <div class="bg-gray-50 dark:bg-gray-900 min-h-screen">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},
  methods: {
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  min-height: 100vh;
  box-sizing: border-box;
}
</style>