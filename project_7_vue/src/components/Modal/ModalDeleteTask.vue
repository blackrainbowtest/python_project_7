<template>
  <div
    id="defaultModal"
    tabindex="-1"
    aria-hidden="true"
    :class="isDelete ? 'fixed' : 'hidden'"
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
                {{ "Deleting" }}
              </h3>
              <button
                type="button"
                class="modal-button text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
                data-modal-hide="defaultModal"
                @click.stop="closeModal"
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
          <div class="px-6 pb-6 pt-2 space-y-2 text-left cursor-auto">
            <div>Are you sure you want to delete this task?</div>
            <!-- suqqess button -->
            <div class="flex justify-center gap-1 lg:gap-4 md:gap-3 sm:gap-2">
              <button
                @click.stop="deleteTaskBtn"
                type="button"
                class="focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"
              >
                YES
              </button>
              <button
                @click.stop="closeModal"
                type="button"
                class="focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800"
              >
                NO
              </button>
              <button
                @click.stop="archiveTaskBtn"
                type="button"
                class="focus:outline-none text-white bg-orange-700 hover:bg-orange-800 focus:ring-4 focus:ring-orange-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-orange-600 dark:hover:bg-orange-700 dark:focus:ring-orange-800"
              >
                ARCHIVE
              </button>
            </div>
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
    return {};
  },
  props: {
    isDelete: {
      type: Boolean,
      required: true,
    },
    taskID: {
      type: Number,
      required: true,
    },
  },
  methods: {
    ...mapActions({ deleteTask: "deleteTask", archiveTask: "archiveTask" }),
    closeModal() {
      this.$emit("closeModal-data");
    },
    async deleteTaskBtn() {
      this.deleteTask(this.taskID);
      this.closeModal();
    },
    archiveTaskBtn() {
      this.archiveTask({ id: this.taskID });
      this.closeModal();
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
