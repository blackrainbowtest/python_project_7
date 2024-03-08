<template>
  <form class="space-y-6" @submit.prevent="submitLogIn">
    <div>
      <label
        for="text"
        class="text-sm font-medium text-gray-900 block mb-2 dark:text-gray-300"
        >Your username</label
      >
      <div class="relative">
        <input
          type="text"
          name="text"
          id="text"
          autocomplete="on"
          class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
          placeholder="Smith78"
          v-model="username"
          required
        />
        <InputAlertComponent
          v-if="errors?.username"
          :errorMessage="errors"
          :errorCount="Number(errors.countDown) ? Number(errors.countDown) : 0"
        />
      </div>
    </div>
    <div>
      <label
        for="password"
        class="text-sm font-medium text-gray-900 block mb-2 dark:text-gray-300"
        >Your password</label
      >
      <div class="relative">
        <input
          type="password"
          name="password"
          id="password"
          autocomplete="current-password"
          placeholder="••••••••"
          class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
          v-model="password"
          required
        />
        <InputAlertComponent
          v-if="errors?.password"
          :errorMessage="errors?.password"
        />
      </div>
    </div>
    <div class="flex items-center justify-center gap-16">
      <div class="flex items-center">
        <div class="flex items-center h-5">
          <input
            id="remember"
            aria-describedby="remember"
            type="checkbox"
            class="cursor-pointer bg-gray-50 border border-gray-300 focus:ring-3 focus:ring-blue-300 h-4 w-4 rounded dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800"
            v-model="checkbox"
          />
        </div>
        <div class="text-sm ml-3">
          <label
            for="remember"
            class="cursor-pointer font-medium text-gray-900 dark:text-gray-300"
            >Remember me</label
          >
        </div>
      </div>
      <div
        @click.stop="toggleForget"
        class="lost-password flex cursor-pointer items-center text-sm text-blue-700 hover:underline dark:text-blue-500"
      >
        Lost Password?
      </div>
    </div>
    <button
      type="submit"
      class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >
      Login to your account
    </button>
  </form>
</template>

<script>
import { mapMutations, mapGetters, mapActions } from "vuex";
import InputAlertComponent from "../InputAlert/InputAlertComponent.vue";

export default {
  data() {
    return {
      username: "",
      password: "",
      checkbox: false,
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
    ...mapGetters({
      getErrors: "getErrors",
      getRecoverySuccess: "getRecoverySuccess",
    }),
  },
  methods: {
    ...mapMutations({ clear: "clear" }),
    ...mapActions({ signIn: "signIn" }),
    async submitLogIn() {
      await this.signIn({
        username: this.username,
        password: this.password,
      });
    },
    checkPassword() {},
    toggleForget() {
      this.$emit("forget-data");
    },
  },
  watch: {
    getErrors: {
      handler() {
        this.errors = this.getErrors;
        if (
          this.username !== "" &&
          this.password !== "" &&
          Object.keys(this.errors).length === 0
        ) {
          this.$emit("accountLogIn-data");
        }
      },
    },
  },
};
</script>
