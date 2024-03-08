<template>
  <div class="w-full flex justify-center">
    <div class="w-[90%] container">
      <div class="overflow-x-auto">
        <table
          v-if="getTasks"
          class="w-full text-sm text-left text-gray-500 dark:text-gray-400"
        >
          <thead
            class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
          >
            <tr>
              <th scope="col" class="px-6 py-3">Task Title</th>
              <th scope="col" class="px-6 py-3">Description</th>
              <th scope="col" class="px-6 py-3">Assigned_to</th>
              <th scope="col" class="px-6 py-3">Created_by</th>
              <th scope="col" class="px-6 py-3">Purpose description</th>
            </tr>
          </thead>
          <tbody>
            <ArchiveTable v-for="task in getTasks()" :key="task.id" :task="task"/>
          </tbody>
        </table>
        <div v-if="!getTasks">
          <div
            class="bg-blue-100 dark:text-blue-100 dark:bg-blue-700 border-t border-b border-blue-500 dark:border-blue-400 text-blue-700 px-4 py-3"
            role="alert"
          >
            <p class="font-bold">Archive is empty</p>
            <p class="text-sm">Archive tasks to archive them.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import ArchiveTable from "./ArchiveTable.vue";

export default {
  data() {
    return {};
  },
  mounted() {
    this.archive();
  },
  components: {
    ArchiveTable,
  },
  computed: {
    ...mapGetters({ getTasks: "getTasks" }),
  },
  methods: {
    ...mapActions({ archive: "archive" }),
  },
};
</script>
