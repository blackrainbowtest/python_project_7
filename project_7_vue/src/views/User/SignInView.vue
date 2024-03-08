<template>
  <section class="w-full bg-gray-800 dark:bg-gray-900">
    <div
      class="w-full flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0"
    >
      <div
        class="w-full bg-gray-800 rounded-lg shadow dark:border md:mt-0 md:max-w-xl sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700"
      >
        <div class="w-full p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1
            class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white"
          >
            Log in to your account
          </h1>
          <form
            class="grid grid-cols-1 md:grid-cols-1 gap-3 md:gap-4"
            @submit.prevent="submit"
          >
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
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="Your user name"
                required=""
                v-model="username"
              />
              {{ errors }}
              <div class="text-xs text-red-600 mt-1" v-show="errors?.login">
                <p v-for="error, idx in errors?.login" :key="idx" class="w-full">
                  {{ error }}
                </p>
              </div>
            </div>
            <div>
              <label
                for="password"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Password</label
              >
              <input
                type="password"
                name="password"
                id="password"
                placeholder="••••••••"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                required=""
                autocomplete="on"
                v-model="password"
              />
            </div>
            <button
              type="submit"
              class="w-full text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            >
              Sign into account
            </button>
            <p class="text-sm font-light text-gray-500 dark:text-gray-400">
              Have'nt an account?
              <router-link
                to="/signup"
                class="font-medium text-blue-600 hover:underline dark:text-blue-500"
                >Create account here</router-link
              >
            </p>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from "vuex";
export default {
  data() {
    return {
      errors: this.getErrors,
      username: "",
      password: "",
      isLoading: false,
    };
  },
  mounted() {
    this.clear()
  },
  computed: {
    ...mapGetters({
      getErrors: "getErrors",
    }),
  },
  methods: {
    ...mapMutations({
      clear: "clear",
    }),
    ...mapActions({
      signIn: "signIn",
    }),
    async submit() {
      await this.signIn({
        username: this.username,
        password: this.password,
      })
    },
  },
  watch: {
    getErrors: {
      handler() {
        this.errors = this.getErrors;
      },
    },
  },
};
</script>

<style></style>
