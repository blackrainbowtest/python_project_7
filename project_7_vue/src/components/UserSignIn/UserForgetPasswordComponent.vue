<template>
  <form class="space-y-6" @submit.prevent="submitLogIn">
    <div
      v-if="getRecoverySuccess"
      class="p-4 text-sm text-blue-800 rounded-lg dark:text-blue-400"
      role="alert"
    >
      <span class="font-bold">Note: </span> {{ getRecoverySuccess }}
    </div>
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
          placeholder="user123"
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
    <button
      type="submit"
      class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >
      Restore password
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
    ...mapActions({ signIn: "signIn", passwordRecover: "passwordRecover" }),
    async submitLogIn() {
      if (this.username.trim()) {
        this.passwordRecover({
            username: this.username,
        });
        // this.$emit("recover-data");
        setTimeout(() => {
          this.clear();
        }, 4000);
      }
    },
    goBack() {
      this.$emit("recover-data");
    },
  },
};
</script>
