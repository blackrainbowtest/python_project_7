<template>
  <section class="w-full bg-gray-50 dark:bg-gray-900 py-32">
    <div
      class="w-full flex flex-col items-center justify-center px-6 py-8 mx-auto lg:py-0"
    >
      <div
        class="w-full relative bg-white rounded-lg shadow dark:border md:mt-0 md:max-w-2xl sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700"
      >
        <div class="w-full p-6 space-y-4 md:space-y-6 sm:p-8">
          <button
            class="bg-orange-300 hover:bg-orange-600 p-2 rounded absolute top-15 right-5"
            @click="isEdit"
          >
            EDIT
          </button>
          <h1
            class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white"
          >
            Your profile
          </h1>
          <form
            class="grid grid-cols-1 md:grid-cols-2 gap-3 md:gap-4"
            @submit.prevent="submit"
          >
            <div>
              <label
                for="first_name"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Your first name</label
              >
              <input
                type="text"
                name="first_name"
                id="first_name"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:disabled:bg-gray-800"
                placeholder="Your first name"
                required=""
                v-model="first_name"
                :disabled="!isAction"
              />
            </div>
            <div>
              <label
                for="last_name"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Your last name</label
              >
              <input
                type="text"
                name="last_name"
                id="last_name"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:disabled:bg-gray-800"
                placeholder="Your last name"
                required=""
                v-model="last_name"
                :disabled="!isAction"
              />
            </div>
            <div>
              <label
                for="username"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Your user name</label
              >
              <input
                type="text"
                name="username"
                id="username"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:disabled:bg-gray-800"
                placeholder="Your user name"
                required=""
                v-model="username"
                :disabled="!isAction"
              />
            </div>
            <div>
              <label
                for="email"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Your email</label
              >
              <input
                type="email"
                name="email"
                id="email"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:disabled:bg-gray-800"
                placeholder="name@company.com"
                required=""
                v-model="email"
                :disabled="!isAction"
              />
            </div>
            <button
              type="submit"
              class="w-50 col-span-2 text-white bg-green-600 hover:bg-green-700 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800 dark:disabled:bg-green-900"
              :disabled="!isAction"
            >
              Save
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  data() {
    return {
      isAction: false,
      errors: {},
      first_name: "",
      last_name: "",
      username: "",
      email: "",
    };
  },
  mounted() {
    this.profile();
    this.first_name = this.getProfile.first_name;
    this.last_name = this.getProfile.last_name;
    this.username = this.getProfile.username;
    this.email = this.getProfile.email;
  },
  computed: {
    ...mapGetters({
      getProfile: "getProfile",
      getErrors: "getErrors",
    }),
  },
  methods: {
    ...mapActions({
      profile: "profile",
      update: "update",
    }),
    isEdit() {
      this.isAction = !this.isAction;
    },
    submit() {
      this.update({
        first_name: this.first_name.trim(),
        last_name: this.last_name.trim(),
        username: this.username.trim(),
        email: this.email.trim(),
      });
      this.isEdit();
    },
  },
  watch: {
    getProfile: {
      handler() {
        this.first_name = this.getProfile.first_name;
        this.last_name = this.getProfile.last_name;
        this.username = this.getProfile.username;
        this.email = this.getProfile.email;
      },
    },
  },
};
</script>

<style></style>
