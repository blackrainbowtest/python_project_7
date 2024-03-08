<template>
  <button
    type="button"
    class="profile flex items-center mr-3 text-sm bg-gray-800 rounded-full md:mr-0 focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600"
    id="user-menu-button"
    aria-expanded="false"
    data-dropdown-toggle="user-dropdown"
    data-dropdown-placement="bottom"
    @click="toggleProfile"
  >
    <span class="sr-only">Open user menu</span>
    <div
      class="relative w-10 h-10 overflow-hidden bg-gray-100 rounded-full dark:bg-gray-600"
    >
      <svg
        class="absolute w-12 h-12 text-gray-400 -left-1"
        fill="currentColor"
        viewBox="0 0 20 20"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          fill-rule="evenodd"
          d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
          clip-rule="evenodd"
        ></path>
      </svg>
    </div>
    <!-- if user have profile image -->
    <img
      v-if="false"
      class="w-8 h-8 rounded-full"
      src="../../assets/user.png"
      alt="user photo"
    />
  </button>
</template>

<script>
export default {
  data() {
    return {};
  },
  props: {},
  methods: {
    toggleProfile() {
      this.$emit("toggleProfile-data");
    },
  },
};
</script>
