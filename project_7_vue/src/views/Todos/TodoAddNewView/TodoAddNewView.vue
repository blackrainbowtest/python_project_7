<template>
  <div class="py-1 px-1">
    <textarea
      id="message"
      rows="2"
      v-model="title"
      class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
      placeholder="Enter a title for this card..."
    ></textarea>
    <div class="flex justify-start items-center gap-4 p-2">
      <!-- suqqess button -->
      <button
        @click="addNewTodo"
        type="button"
        class="focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"
      >
        Add Card
      </button>
      <!-- close Button -->
      <button
        @click="toggleAnotherCard"
        type="button"
        class="bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg px-2 py-2 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-900"
      >
        <span class="sr-only">Close menu</span>
        <!-- Heroicon name: outline/x -->
        <svg
          class="h-6 w-6 text-white"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          stroke="currentColor"
          aria-hidden="true"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      title: "",
    };
  },
  props: {
    category: {
      type: Number,
      required: true,
    },
  },
  methods: {
    ...mapActions({ addTask: "addTask" }),
    toggleAnotherCard() {
      this.$emit("toggleAnotherCard-data");
    },
    addNewTodo() {
      if (this.title.trim()) {
        this.addTask({
          title: this.title,
          categories: this.category,
        });
        this.title = "";
      }
    },
  },
};
</script>
