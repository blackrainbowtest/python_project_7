<template>
  <form class="space-y-6" @submit.prevent="submitRegistration">
    <div class="grid gap-6 mb-6 md:grid-cols-2">
      <div class="">
        <label
          for="first_name"
          class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
          >First name</label
        >
        <div class="relative">
          <input
            type="text"
            id="first_name"
            class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
            placeholder="John"
            requiredd
            autocomplete="on"
            v-model="first_name"
          />
          <InputAlertComponent
            v-if="errors?.first_name"
            :errorMessage="errors?.first_name"
          />
        </div>
      </div>
      <div>
        <label
          for="last_name"
          class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
          >Last name</label
        >
        <div class="relative">
          <input
            type="text"
            id="last_name"
            class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
            placeholder="Doe"
            requiredd
            autocomplete="on"
            v-model="last_name"
          />
          <InputAlertComponent
            v-if="errors?.last_name"
            :errorMessage="errors?.last_name"
          />
        </div>
      </div>
      <div>
        <label
          for="username"
          class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
          >Username</label
        >
        <div class="relative">
          <input
            type="text"
            id="username"
            class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
            placeholder="Smith97"
            requiredd
            autocomplete="username"
            v-model="username"
          />
          <InputAlertComponent
            v-if="errors?.username"
            :errorMessage="errors?.username"
          />
        </div>
      </div>
      <div>
        <label
          for="email"
          class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
          >Email</label
        >
        <div class="relative">
          <input
            type="text"
            id="email"
            class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
            placeholder="user@gmail.com"
            requiredd
            autocomplete="on"
            v-model="email"
          />
          <InputAlertComponent
            v-if="errors?.email"
            :errorMessage="errors?.email"
          />
        </div>
      </div>
      <div>
        <label
          @input="checkPassword"
          for="password"
          class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
          >Password</label
        >
        <div class="relative">
          <input
            type="password"
            id="password"
            class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
            placeholder="••••••••"
            requiredd
            autocomplete="new-password"
            v-model="password1"
          />
          <InputAlertComponent
            v-if="errors?.password1"
            :errorMessage="errors?.password1"
          />
        </div>
      </div>
      <div>
        <label
          for="password-confirm"
          class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
          >Confirm</label
        >
        <div class="relative">
          <input
            type="password"
            id="password-confirm"
            class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
            placeholder="••••••••"
            requiredd
            autocomplete="new-password"
            v-model="password2"
          />
          <InputAlertComponent
            v-if="errors?.password2"
            :errorMessage="errors?.password2"
          />
        </div>
      </div>
    </div>
    <button
      type="submit"
      class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >
      Create new account
    </button>
  </form>
</template>

<script>
import { mapMutations, mapGetters, mapActions } from "vuex";
import InputAlertComponent from "../InputAlert/InputAlertComponent.vue";

export default {
  data() {
    return {
      first_name: "",
      last_name: "",
      username: "",
      email: "",
      password1: "",
      password2: "",
      errors: this.getErrors,
    };
  },
  components: {
    InputAlertComponent,
  },
  mounted() {
    this.clear();
  },
  computed: {
    ...mapGetters({ getErrors: "getErrors" }),
  },
  methods: {
    ...mapMutations({ clear: "clear" }),
    ...mapActions({ signUp: "signUp" }),
    submitRegistration() {
      this.signUp({
        first_name: this.first_name,
        last_name: this.last_name,
        username: this.username,
        email: this.email,
        password1: this.password1,
        password2: this.password2,
      })
    },
    checkPassword() {},
  },
  watch: {
    getErrors: {
      handler() {
        this.errors = this.getErrors;
        if(this.first_name !== "" && this.last_name !== "" && this.username !== "" && this.email !== "" && this.password1 !== ""
        && this.password2 !== "" && Object.keys(this.errors).length === 0) {
          this.$emit("accountCreated-data");
        }
      },
    },
  },
};
</script>
