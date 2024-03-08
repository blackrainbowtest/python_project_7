<template>
  <div
    id="defaultModal"
    tabindex="-1"
    aria-hidden="true"
    :class="isInvite ? 'fixed' : 'hidden'"
    class="top-0 cursor-auto left-0 right-0 z-50 w-full overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%)] max-h-full"
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
                {{ "Invite your friend" }}
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
              @submit.prevent="sendInviteBtn"
              class="px-6 pb-6 pt-2 space-y-2 text-left cursor-auto"
            >
              <div>
                <label
                  for="email"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Your friend's email</label
                >
                <input
                  type="email"
                  name="email"
                  id="email"
                  class="text-gray-900 bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="name@company.com"
                  required=""
                  v-model="email"
                />
              </div>
              <div>
                <textarea
                  id="message"
                  rows="2"
                  v-model="message"
                  class="resize-none block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Enter some message..."
                  required
                ></textarea>
              </div>
              <!-- suqqess button -->
              <div class="flex justify-center gap-1 lg:gap-4 md:gap-3 sm:gap-2">
                <button
                  type="submit"
                  class="focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                >
                  YES
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      email: "",
      message: "",
    };
  },
  props: {
    isInvite: {
      type: Boolean,
      required: true,
    },
  },
  methods: {
    ...mapActions({ sendInvite: "sendInvite" }),
    closeInvite() {
      this.$emit("closeInvite-data");
    },
    sendInviteBtn() {
      this.sendInvite({
        email: this.email,
        message: this.message,
      });
      this.email = ''
      this.message = ''
      this.$emit("closeInvite-data");
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
