<template>
  <div
    class="items-center justify-between w-full md:flex md:w-auto md:order-1"
    :class="showMenu ? 'block' : 'hidden'"
    id="mobile-menu-2"
  >
    <ul
      class="flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700"
    >
      <li>
        <router-link
          to="/"
          class="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
          aria-current="page"
          >Home</router-link
        >
      </li>
      <li>
        <router-link
          to="/todos"
          class="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
          >Todos</router-link
        >
      </li>
      <li>
        <router-link
          to="/archive"
          class="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
          >Archive</router-link
        >
      </li>
      <!-- <li>
        <a
          href="#"
          class="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
          >Pricing</a
        >
      </li>
      <li>
        <router-link
          to="/"
          class="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
          >Contact</router-link
        >
      </li> -->
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  props: {
    showMenu: {
      type: Boolean,
      required: true,
    },
  },
  methods: {
    toggleNav() {
      this.$emit("toggleNav-data");
    },
  },
};
</script>

<style scoped>
a.router-link-exact-active {
  color: #0000f2;
}
/* dark theme */
html.dark a.router-link-exact-active {
  color: #95db4a;
}
</style>
