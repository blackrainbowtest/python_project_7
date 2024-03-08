<template>
  <div
    @click.prevent="editTodo"
    :class="isRename ? '' : ''"
    class="relative z-auto todo-item cursor-pointer font-normal px-2 py-1 text-left bg-white hover:bg-slate-100 dark:bg-gray-700 dark:hover:bg-gray-800 text-gray-700 dark:text-gray-400 rounded-md border-2 border-gray-200 dark:border-gray-600"
  >
    {{ task.title }}
    <div
      @click.stop="deleteTodo"
      class="absolute z-20 delete-button top-1 px-2 right-1 rounded-lg hover:bg-gray-300 dark:hover:bg-gray-600"
    >
      X
    </div>
    <div
      @click.stop="renameTodo"
      class="absolute z-20 edit-button top-1 right-[30px] rounded-lg hover:bg-gray-300 dark:hover:bg-gray-600"
    >
      <svg
        width="24"
        height="24"
        viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:xlink="http://www.w3.org/1999/xlink"
      >
        <rect width="24" height="24" stroke="none" fill="#101101" opacity="0" />

        <g transform="matrix(0.44 0 0 0.44 12 12)">
          <path
            style="
              stroke: none;
              stroke-width: 1;
              stroke-dasharray: none;
              stroke-linecap: butt;
              stroke-dashoffset: 0;
              stroke-linejoin: miter;
              stroke-miterlimit: 4;
              fill-rule: nonzero;
              opacity: 0.6;
            "
            class="fill-gray-900 dark:fill-gray-200"
            transform=" translate(-25.29, -22.22)"
            d="M 26.273438 4.445313 C 26.148438 4.457031 26.027344 4.476563 25.902344 4.5 C 24.902344 4.699219 23.800781 5.5 22.800781 6.5 L 27.597656 9.5 C 28.199219 7.5 28.601563 5.5 27.300781 4.699219 C 27 4.472656 26.644531 4.417969 26.273438 4.445313 Z M 21.402344 8 C 20.199219 9.5 17.5 13 14.699219 17.402344 C 13.800781 18.800781 12.898438 20.402344 12 21.902344 C 12 22.800781 11.902344 23.601563 11.800781 24.402344 C 11.5 26.300781 11 27.898438 10.699219 28.5 C 10.300781 29.601563 9.699219 30.398438 9.101563 31 L 12.902344 33.402344 C 13.5 32.601563 14.5 31.199219 15.699219 29.597656 L 15.097656 29.199219 C 12.800781 28 11.699219 25.300781 12.597656 22.800781 C 13.300781 20.800781 15.300781 19.5 17.402344 19.5 C 17.800781 19.5 18.199219 19.597656 18.699219 19.699219 L 21.800781 20.5 C 24.199219 16.5 26 12.898438 26.800781 11.199219 Z M 16.902344 10.800781 L 10 11.800781 C 9.300781 11.902344 8.800781 12.300781 8.5 12.902344 L 2.898438 25.5 C 2.699219 26 2.5 26.699219 2.601563 27.300781 C 2.699219 28.402344 3.199219 29.398438 4 30.097656 C 5.101563 30.800781 6.398438 30.601563 7 30.300781 C 8.398438 29.699219 8.898438 27.800781 9 27.300781 C 9.300781 26.199219 10.300781 23.199219 9.898438 20.300781 L 10.800781 20.199219 C 11.5 18.898438 12.300781 17.699219 13 16.5 C 14.398438 14.300781 15.699219 12.402344 16.902344 10.800781 Z M 28.5 12.597656 C 27.800781 14.097656 26.101563 17.5 23.800781 21.300781 L 26.402344 22 L 28.402344 22.597656 L 27.300781 24.199219 L 18.199219 21.800781 C 16.699219 21.402344 15.101563 22.199219 14.5 23.699219 C 13.898438 25.199219 14.601563 26.898438 16 27.597656 L 27.402344 34 C 29.101563 34.898438 31 35.199219 32.902344 34.902344 C 33.101563 34.902344 40.902344 33.097656 40.902344 33.097656 L 38.800781 18.902344 L 28.800781 12.699219 C 28.699219 12.597656 28.601563 12.597656 28.5 12.597656 Z M 45.300781 17.402344 L 40.699219 18.097656 L 43.402344 35.699219 L 48 35 Z M 6.898438 32.097656 C 5.800781 35.199219 5.800781 37.199219 5.800781 38 L 5.101563 39 C 4.898438 39.300781 5 39.699219 5.300781 39.902344 C 5.5 40 5.601563 40 5.800781 40 C 6 39.898438 6.101563 39.800781 6.300781 39.699219 L 6.898438 38.699219 C 7.601563 38.398438 9.398438 37.5 11.699219 35.097656 Z"
            stroke-linecap="round"
          />
        </g>
      </svg>
    </div>
    <div v-if="isRename" class="absolute z-50 w-full top-0 left-0 cursor-auto">
      <div
        class="flex flex-col z-50 gap-2 items-start justify-start rename-item"
      >
        <textarea
          id="message"
          rows="4"
          v-model="title"
          class="resize-none block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-md border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="Enter a more detailed description..."
        ></textarea>
        <button
          @click="changeTitle"
          type="button"
          class="focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"
        >
          Save
        </button>
      </div>
    </div>
    <ModalDeleteTask :isDelete="isDelete" @closeModal-data="closeModal" :taskID="task.id" />
  </div>
</template>

<script>
import { mapActions } from "vuex";
import ModalDeleteTask from "@/components/Modal/ModalDeleteTask.vue";

export default {
  data() {
    return {
      isAnotherCard: false,
      isRename: false,
      isDelete: false,
      title: this.task.title,
    };
  },
  components: {
    ModalDeleteTask,
  },
  props: {
    task: {
      type: Object,
      required: true,
    },
  },
  methods: {
    ...mapActions({ updateTitle: "updateTitle" }),
    editTodo() {
      if (!this.isRename && !this.isDelete) {
        this.$emit("editTodo-data", this.task);
      }
    },
    renameTodo() {
      this.isRename = true;
      document.addEventListener("click", this.closeWhenClickedOutside);
    },
    deleteTodo() {
      this.isDelete = true;
      document.addEventListener("click", this.closeWhenClickedOutside);
    },
    changeTitle() {
      this.isRename = false;
      document.removeEventListener("click", this.closeWhenClickedOutside);
      this.updateTitle({
        id: this.task.id,
        title: this.title,
        categories: this.task.categories.id,
      });
    },
    closeWhenClickedOutside(event) {
      if (
        !event.target.closest(".rename-item") &&
        !event.target.closest(".edit-button") &&
        !event.target.closest(".modal-delete") &&
        !event.target.closest(".delete-button")
      ) {
        this.isRename = false;
        this.isDelete = false;
        document.removeEventListener("click", this.closeWhenClickedOutside);
      }
    },
    closeModal() {
      this.isDelete = false;
      document.removeEventListener("click", this.closeWhenClickedOutside);
    },
  },
};
</script>

<style scoped>
.todo-item .edit-button {
  display: none;
}
.todo-item:hover .edit-button {
  display: block;
}

.popapBg {
  background-color: #000000a7;
}
</style>
