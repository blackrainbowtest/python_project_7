<template>
  <div class="w-full flex justify-center">
    <div class="w-[90%] container">
      <div
        v-if="getCategories"
        class="grid p-1 min-w-[350px] content-center grid-cols-1 gap-1 lg:grid-cols-4 lg:gap-4 md:grid-cols-3 mdg:gap-3 sm:grid-cols-2 sm:gap-2"
      >
        <!-- category list -->
        <TodoListView
          v-for="category in getCategories"
          :key="category.id"
          :category="category"
          @editTodo-data="editTodo"
        />
        <!-- add new category list button -->
        <div class="select-none">
          <div
            class="cursor-pointer rounded-md text-left py-1 px-4 text-base tracking-tight text-gray-500 dark:text-white hover:text-gray-600 hover:dark:text-slate-200 hover:bg-gray-200 bg-gray-100 dark:bg-gray-800 dark:hover:bg-gray-700"
          >
            <span>+ Add another list</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <ModalTask
    v-if="isModal"
    :isModal="isModal"
    :editTask="editTask"
    @closeModal-data="closeModal"
  />
</template>

<script>

import { mapGetters, mapActions } from "vuex";
import TodoListView from "../TodoListView/TodoListView.vue";
import ModalTask from "@/components/Modal/ModalTask.vue";

export default {
  data() {
    return {
      isModal: false,
      editTask: {},
    };
  },
  mounted() {
    this.categories();
  },
  components: {
    TodoListView,
    ModalTask,
  },
  computed: {
    ...mapGetters({ getTasks: "getTasks", getCategories: "getCategories" }),
  },
  methods: {
    ...mapActions({ tasks: "tasks", categories: "categories" }),
    toggleEditing() {
      this.isModal = true;
      document.addEventListener("click", this.closeWhenClickedOutside);
    },
    closeWhenClickedOutside(event) {
      if (
        !event.target.closest(".modal-body") &&
        !event.target.closest(".todo-item")
      ) {
        this.isModal = false;
        document.removeEventListener("click", this.closeWhenClickedOutside);
      }
    },
    editTodo(data) {
      this.toggleEditing();
      this.editTask = data;
    },
    closeModal() {
      this.isModal = false;
      document.removeEventListener("click", this.closeWhenClickedOutside);
    },
  },
};
</script>
