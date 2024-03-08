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
        <div class="relative bg-gray-200 rounded-lg shadow dark:bg-gray-700">
          <!-- Modal header -->
          <div class="p-4 rounded-t">
            <!-- first row -->
            <div class="flex items-start justify-between">
              <h3
                class="text-xl font-semibold text-gray-900 dark:text-white uppercase"
              >
                {{ editTask.title }}
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
            <div class="flex items-start justify-between">
              <span class="font-semibold text-gray-500 dark:text-gray-200"
                >in list {{ editTask?.categories?.name }}</span
              >
            </div>
          </div>
          <!-- Modal body -->
          <div class="p-6 space-y-2 text-left cursor-auto">
            <textarea
              id="message"
              rows="4"
              v-model="description"
              class="resize-none block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Enter a more detailed description..."
            ></textarea>
            <!-- suqqess button -->
            <button
              @click="changeDescription"
              type="button"
              class="focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"
            >
              Save
            </button>
          </div>
          <!-- Modal footer -->
          <div
            class="flex w-full justify-center items-center p-6 gap-4 border-t border-gray-200 rounded-b dark:border-gray-600"
          >
            <div v-if="editTask?.assigned_to">
              <span class="font-semibold text-gray-500 dark:text-gray-200"
                >assigned to: {{ editTask?.assigned_to?.username }}</span
              >
            </div>
            <div v-if="!editTask?.assigned_to && editTask?.categories?.id == 4">
              <span class="font-semibold text-gray-500 dark:text-gray-200"
                >assigned to: Noone</span
              >
            </div>
            <form
              v-if="!editTask?.assigned_to && editTask?.categories?.id < 4"
              class="flex flex-col gap-2 text-sm font-medium text-gray-500 dark:text-gray-300"
              @submit.prevent="assign"
            >
              <div class="flex gap-2">
                <span class="font-semibold text-gray-500 dark:text-gray-200"
                  >assign to someone:</span
                >
                <select
                  id="countries"
                  v-model="developer"
                  required
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                >
                  <option selected value="0">Choose a country</option>
                  <option
                    v-for="developer in getDevelopers"
                    :key="developer.id"
                    :value="developer.id"
                  >
                    {{ developer.username }}
                  </option>
                </select>
              </div>
              <div class="flex gap-2 items-end">
                <textarea
                  id="message"
                  rows="2"
                  v-model="assignDescription"
                  class="resize-none block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Enter a more detailed description..."
                  required
                ></textarea>
                <button
                  type="submit"
                  class="focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"
                >
                  Assign
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
import { mapActions, mapGetters } from "vuex";

export default {
  data() {
    return {
      description: this.editTask.description,
      developer: 0,
      assignDescription: "",
    };
  },
  mounted() {
    this.developers();
  },
  computed: {
    ...mapGetters({ getDevelopers: "getDevelopers" }),
  },
  props: {
    isModal: {
      type: Boolean,
      required: true,
    },
    editTask: {
      type: Object,
      required: true,
    },
  },
  methods: {
    ...mapActions({
      updateDescription: "updateDescription",
      developers: "developers",
      updateAssigned: "updateAssigned",
    }),
    closeModal() {
      this.$emit("closeModal-data");
    },
    changeDescription() {
      if (this.description && this.description.trim()) {
        this.updateDescription({
          id: this.editTask.id,
          description: this.description,
          categories: this.editTask.categories.id,
        });
        this.closeModal();
      }
    },
    assign() {
      if (this.developer && this.assignDescription.trim()) {
        this.updateAssigned({
          task: this.editTask.id,
          assigned_to: this.developer,
          description: this.assignDescription,
          categories: this.editTask.categories.id,
        });
        this.closeModal();
      }
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
