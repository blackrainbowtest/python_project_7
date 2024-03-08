<template>
  <div
    id="defaultModal"
    tabindex="-1"
    aria-hidden="true"
    class="fixed top-0 cursor-auto left-0 right-0 z-50 w-full overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%)] max-h-full"
  >
    <div
      class="flex w-full h-[calc(100%)] max-h-full justify-center items-center shadow popapBg"
    >
      <div class="relative w-1/3 min-w-[350px] max-w-2xl max-h-full modal-body">
        <!-- Modal content -->
        <div
          class="relative bg-gray-200 rounded-lg shadow dark:bg-gray-700 modal-delete"
        >
          <!-- Modal header -->
          <div class="p-4 rounded-t">
            <!-- first row -->
            <div class="flex items-start justify-between">
              <h3
                class="text-xl font-semibold text-gray-900 dark:text-white uppercase"
              >
                {{ "Change your password" }}
              </h3>
              <button
                type="button"
                class="modal-button text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
                data-modal-hide="defaultModal"
                @click.stop="closeInvite"
              >
                <svg
                  aria-hidden="true"
                  class="w-5 h-5"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill-rule="evenodd"
                    d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                    clip-rule="evenodd"
                  ></path>
                </svg>
                <span class="sr-only">Close modal</span>
              </button>
            </div>
          </div>
          <!-- Modal body -->
          <div>
            <form
              class="px-6 pb-6 pt-2 space-y-2 text-left cursor-auto"
              @submit.prevent="submitChange"
            >
              <div>
                <label
                  for="password"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >New password</label
                >
                <div class="relative">
                  <input
                    type="password"
                    id="password"
                    class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                    placeholder="••••••••"
                    required
                    autocomplete="password"
                    v-model="password1"
                  />
                  <InputAlertComponent
                    v-if="errors?.new_password1"
                    :errorMessage="errors?.new_password1"
                  />
                </div>
              </div>
              <div class="pb-4">
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
                    required
                    autocomplete="password"
                    v-model="password2"
                  />
                  <InputAlertComponent
                    v-if="errors?.new_password2"
                    :errorMessage="errors?.new_password2"
                  />
                </div>
              </div>

              <button
                type="submit"
                class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
              >
                Change password
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import InputAlertComponent from "@/components/InputAlert/InputAlertComponent.vue";
import router from '@/router'

export default {
  data() {
    return {
      password1: "",
      password2: "",
      errors: this.getErrors,
    };
  },
  components: {
    InputAlertComponent,
  },
  props: {
    isPassword: {
      type: Boolean,
      required: true,
    },
  },
  computed: {
    ...mapGetters({ getErrors: "getErrors" }),
  },
  methods: {
    ...mapActions({ passwordChange: "passwordChange" }),
    closeInvite() {
      this.$emit("closePassword-data");
      router.push('/')
    },
    submitChange() {
      this.passwordChange({
        new_password1: this.password1,
        new_password2: this.password2,
        shortcode: this.$route.query?.shortcode,
        username: this.$route.query?.username
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

<style scoped>
html.dark .popapBg {
  background-color: #ffffffa7;
}
.popapBg {
  background-color: #000000a7;
}
</style>
