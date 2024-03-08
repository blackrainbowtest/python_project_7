<template>
  <section class="w-full bg-gray-800 dark:bg-gray-900">
    <div
      class="w-full flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0"
    >
      <div
        class="w-full bg-gray-800 rounded-lg shadow dark:border md:mt-0 md:max-w-2xl sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700"
      >
        <div class="w-full p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1
            class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white"
          >
            Create a new account
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
                class=" bg-gray-800 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="Your first name"
                required=""
                v-model="first_name"
              />
              <div
                class="text-xs text-red-600 mt-1"
                v-show="errors?.first_name"
              >
                <p
                  v-for="(error, idx) in errors?.first_name"
                  :key="idx"
                  class="w-full"
                >
                  {{ error }}
                </p>
              </div>
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
                class="bg-gray-800 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="Your last name"
                required=""
                v-model="last_name"
              />
              <div class="text-xs text-red-600 mt-1" v-show="errors?.last_name">
                <p
                  v-for="(error, idx) in errors?.last_name"
                  :key="idx"
                  class="w-full"
                >
                  {{ error }}
                </p>
              </div>
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
                class="bg-gray-800 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="Your user name"
                required=""
                v-model="username"
              />
              <div class="text-xs text-red-600 mt-1" v-show="errors?.username">
                <p
                  v-for="(error, idx) in errors?.username"
                  :key="idx"
                  class="w-full"
                >
                  {{ error }}
                </p>
              </div>
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
                class="bg-gray-800 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="name@company.com"
                required=""
                v-model="email"
              />
              <div class="text-xs text-red-600 mt-1" v-show="errors?.email">
                <p
                  v-for="(error, idx) in errors?.email"
                  :key="idx"
                  class="w-full"
                >
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
                class="bg-gray-800 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                required=""
                autocomplete="on"
                v-model="password1"
              />
              <div class="text-xs text-red-600 mt-1" v-show="errors?.password1">
                <p
                  v-for="(error, idx) in errors?.password1"
                  :key="idx"
                  class="w-full"
                >
                  {{ error }}
                </p>
              </div>
            </div>
            <div>
              <label
                for="confirm-password"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Confirm password</label
              >
              <input
                type="password"
                name="confirm-password"
                id="confirm-password"
                placeholder="••••••••"
                class="bg-gray-800 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                required=""
                autocomplete="on"
                v-model="password2"
              />
              <div class="text-xs text-red-600 mt-1" v-show="errors?.password2">
                <p
                  v-for="(error, idx) in errors?.password2"
                  :key="idx"
                  class="w-full"
                >
                  {{ error }}
                </p>
              </div>
            </div>
            <button
              type="submit"
              class="w-full text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            >
              Sign in account
            </button>
            <p class="text-sm font-light text-gray-500 dark:text-gray-400">
              Already have an account?
              <router-link
                to="/signin"
                class="font-medium text-blue-600 hover:underline dark:text-blue-500"
                >Login here</router-link
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
      first_name: "",
      last_name: "",
      username: "",
      email: "",
      password1: "",
      password2: "",
    };
  },
  mounted() {
    this.clear();
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
      signUp: "signUp",
    }),
    submit() {
      this.signUp({
        first_name: this.first_name,
        last_name: this.last_name,
        username: this.username,
        email: this.email,
        password1: this.password1,
        password2: this.password2,
      });
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
