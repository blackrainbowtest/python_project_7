<template>
  <div
    id="defaultModal"
    tabindex="-1"
    aria-hidden="true"
    :class="isModal ? 'fixed' : 'hidden'"
    class="top-0 left-0 right-0 z-50 w-full overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%)] max-h-full"
  >
    <div
      class="flex w-full h-[calc(100%)] max-h-full justify-center items-center shadow popapBg"
    >
      <div class="relative w-full max-w-2xl max-h-full modal-body">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
          <!-- Modal header -->
          <div
            class="flex items-start justify-between p-4 border-b rounded-t dark:border-gray-600"
          >
            <h3
              class="text-xl font-semibold text-gray-900 dark:text-white uppercase"
            >
              {{ isRegistred ? "Sign in" : "Sign Up" }}
            </h3>
            <button
              type="button"
              class="modal-button text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
              data-modal-hide="defaultModal"
              @click="closeModal"
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
          <!-- Modal body -->
          <div class="p-6 space-y-6">
            <UserSignInComponent v-if="!isForget && isRegistred" @accountLogIn-data="checkIsLogIn" @forget-data="forget"/>
            <UserForgetPasswordComponent v-else-if="isForget" @recover-data="recover"/>
            <UserSignUpComponent v-if="!isRegistred" @accountCreated-data="checkIsRegistred"/>
          </div>
          <!-- Modal footer -->
          <div
            class="flex w-full justify-center items-center p-6 gap-4 border-t border-gray-200 rounded-b dark:border-gray-600"
          >
            <div
              class="flex gap-2 text-sm font-medium text-gray-500 dark:text-gray-300"
            >
              {{ isRegistred ? "Not registered?" : "Already have an account?" }}
              <div
                @click="checkIsRegistred"
                class="cursor-pointer text-blue-700 hover:underline dark:text-blue-500 hover:text-blue-800 hover:dark:text-blue-300"
              >
                {{ isRegistred ? "Create account" : "Log in" }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import UserSignInComponent from "@/components/UserSignIn/UserSignInComponent.vue";
import UserSignUpComponent from "@/components/UserSignUp/UserSignUpComponent.vue";
import UserForgetPasswordComponent from "@/components/UserSignIn/UserForgetPasswordComponent.vue";
export default {
  data() {
    return {
      isRegistred: true,
      isForget: false,
    };
  },
  components: {
    UserSignInComponent,
    UserSignUpComponent,
    UserForgetPasswordComponent,
},
  mounted() {},
  props: {
    isModal: {
      type: Boolean,
      required: true,
    },
  },
  methods: {
    closeModal() {
      this.$emit("closeModal-data");
    },
    checkIsRegistred() {
      this.isRegistred = !this.isRegistred;
      this.isForget = false;
    },
    checkIsLogIn() {
      this.$emit("logIn-data");
    },
    forget() {
      this.isForget = true
      this.isRegistred = true
    },
    recover() {
      this.isForget = false
      this.isRegistred = true
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
