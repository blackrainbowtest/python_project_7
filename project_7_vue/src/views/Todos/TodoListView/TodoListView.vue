<template>
  <div class="">
    <div
      class="block p-2 bg-gray-100 border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700"
    >
      <div class="py-2 px-1">
        <h5
          class="text-left text-xl font-bold tracking-tight text-gray-900 dark:text-white"
        >
          {{ category?.name }}
        </h5>
      </div>
      <draggable
        v-model="myTasks"
        group="todoList"
        @start="drag = true"
        @end="drag = false"
        item-key="id"
        :animation="300"
      >
        <template #item="{ element: task }">
          <div class="flex flex-col gap-1 py-1 px-1 select-none">
            <TodoView :task="task" @editTodo-data="editTodo" />
          </div>
        </template>
      </draggable>
      <TodoAddNewView
        v-if="isAnotherCard"
        @toggleAnotherCard-data="toggleAnotherCard"
        :category="category.id"
      />
      <div
        v-if="!isAnotherCard"
        @click="toggleAnotherCard"
        class="cursor-pointer rounded-md text-left py-1 px-4 text-base tracking-tight text-gray-500 dark:text-white hover:text-gray-600 hover:dark:text-slate-200 hover:bg-gray-200 bg-gray-100 dark:bg-gray-800 dark:hover:bg-gray-700"
      >
        + Add another card
      </div>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";
import { mapGetters, mapActions } from "vuex";
import TodoView from "../TodoView/TodoView.vue";
import TodoAddNewView from "../TodoAddNewView/TodoAddNewView.vue";

export default {
  data() {
    return {
      isAnotherCard: false,
    };
  },
  mounted() {
    this.tasks(this.category?.id);
  },
  props: {
    category: {
      type: Object,
      required: true,
    },
  },
  components: {
    TodoView,
    TodoAddNewView,
    draggable,
  },
  computed: {
    ...mapGetters({ getTasks: "getTasks" }),
    // ---------------------------------------------------------------
    myTasks: {
      get() {
        return this.getTasks(this.category?.name);
      },
      set(value) {
        this.updateDraggable({ categories: this.category.id, tasks: value });
      },
    },
  },
  methods: {
    ...mapActions({ tasks: "tasks", updateDraggable: "updateDraggable" }),
    toggleAnotherCard() {
      this.isAnotherCard = !this.isAnotherCard;
    },
    editTodo(data) {
      this.$emit("editTodo-data", data);
    },
  },
};
</script>
