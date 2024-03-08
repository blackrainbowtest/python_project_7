<template>
  <div
    class="select-none z-auto my-4 w-40 text-base list-none bg-white divide-y divide-gray-100 rounded-lg shadow dark:bg-gray-700 dark:divide-gray-600"
    :class="showProfile ? 'block profile-class' : 'hidden'"
    id="user-dropdown"
  >
    <div class="px-4 py-3">
      <span v-if="isUser" class="block text-sm text-gray-900 dark:text-white"
        >{{ profile?.main?.username }}</span
      >
      <span
        v-if="isUser"
        class="block text-sm text-gray-500 truncate dark:text-gray-400"
        >{{ profile?.main?.email }}</span
      >
      <span
        v-if="!isUser"
        @click="openModal"
        class="modal-button py-2 rounded-xl cursor-pointer block text-sm text-blue-500 truncate dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 hover:bg-gray-100 dark:hover:bg-gray-600"
        >Sign In</span
      >
    </div>
    <ul class="py-2" aria-labelledby="user-menu-button">
      <li>
        <div
          class="block px-4 py-2 text-sm text-gray-700 dark:text-gray-200 dark:hover:text-white"
        >
          <div class="w-full flex justify-center gap-4">
            <div
              class="cursor-pointer rounded-xl hover:bg-gray-100 dark:hover:bg-gray-600"
              @click="lightMode"
            >
              <svg
                class="h-5 w-5 fill-yellow-500 dark:fill-yellow-300"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
              >
                <path
                  d="M7 12a5 5 0 1 1 5 5 5 5 0 0 1-5-5zm5-7a1 1 0 0 0 1-1V3a1 1 0 0 0-2 0v1a1 1 0 0 0 1 1zm-1 15v1a1 1 0 0 0 2 0v-1a1 1 0 0 0-2 0zm10-9h-1a1 1 0 0 0 0 2h1a1 1 0 0 0 0-2zM3 13h1a1 1 0 0 0 0-2H3a1 1 0 0 0 0 2zm14.657-5.657a1 1 0 0 0 .707-.293l.707-.707a1 1 0 1 0-1.414-1.414l-.707.707a1 1 0 0 0 .707 1.707zM5.636 16.95l-.707.707a1 1 0 1 0 1.414 1.414l.707-.707a1 1 0 0 0-1.414-1.414zm11.314 0a1 1 0 0 0 0 1.414l.707.707a1 1 0 0 0 1.414-1.414l-.707-.707a1 1 0 0 0-1.414 0zM5.636 7.05A1 1 0 0 0 7.05 5.636l-.707-.707a1 1 0 0 0-1.414 1.414z"
                />
              </svg>
            </div>
            <div class="cursor-pointer rounded-xl" @click="defaultMode">
              <svg
                class="h-5 w-5 fill-gray-600 dark:fill-gray-300"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
              >
                <path
                  d="M11 4V3a1 1 0 0 1 2 0v1a1 1 0 0 1-2 0zM5.636 7.05A1 1 0 0 0 7.05 5.636l-.707-.707a1 1 0 0 0-1.414 1.414zM19 12a1 1 0 0 0 1 1h1a1 1 0 0 0 0-2h-1a1 1 0 0 0-1 1zm-.636-4.95.707-.707a1 1 0 1 0-1.414-1.414l-.707.707a1 1 0 0 0 1.414 1.414zM22 18a4 4 0 0 1-4 4H8.729A6.729 6.729 0 0 1 2 15.271a6.254 6.254 0 0 1 4.741-6.128A5.989 5.989 0 0 1 18 12a5.864 5.864 0 0 1-.109 1.09A4.993 4.993 0 0 1 22 18zm-6-6a3.982 3.982 0 0 0-6.778-2.853 5.971 5.971 0 0 1 4.542 4.3 5.823 5.823 0 0 1 2.1-.449A3.824 3.824 0 0 0 16 12z"
                />
              </svg>
            </div>
            <div class="cursor-pointer rounded-xl" @click="darkMode">
              <svg
                class="h-5 w-5 fill-sky-600 dark:fill-sky-300"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
              >
                <path
                  d="M11.993,3a9.326,9.326,0,0,0-1.138,4.477,8.8,8.8,0,0,0,8.569,9.015c.2,0,.385-.017.576-.03A8.5,8.5,0,0,1,12.569,21,8.8,8.8,0,0,1,4,11.985,8.83,8.83,0,0,1,11.993,3Z"
                />
              </svg>
            </div>
          </div>
        </div>
      </li>
      <li v-if="isUser">
        <div
          class="cursor-pointer block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"
        >
          Settings
        </div>
      </li>
      <li v-if="isUser">
        <div
          @click="invite"
          class="cursor-pointer block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"
        >
          Invite friend
        </div>
      </li>
      <li v-if="isUser">
        <div
          @click="userSignOut"
          class="cursor-pointer block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"
        >
          Sign out
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {};
  },
  props: {
    showProfile: {
      type: Boolean,
      required: true,
    },
    isUser: {
      type: Boolean,
      required: true,
    },
    profile: {
      type: Object,
      required: true,
    },
  },
  methods: {
    ...mapActions({ logout: "logout" }),
    lightMode() {
      this.$emit("lightMode-data");
    },
    defaultMode() {
      this.$emit("defaultMode-data");
    },
    darkMode() {
      this.$emit("darkMode-data");
    },
    openModal() {
      this.$emit("openModal-data");
    },
    userSignOut() {
      this.logout();
      this.$emit("logoutSuccess-data");
    },
    invite(){
      this.$emit("invite-data");
    },
  },
};
</script>

<style scoped>
.profile-class {
  position: absolute;
  right: 0;
  inset: 0px auto auto 0px;
  margin: 0px;
  transform: translate3d(calc(100vw - 160px), 60.4px, 0px);
}
</style>
