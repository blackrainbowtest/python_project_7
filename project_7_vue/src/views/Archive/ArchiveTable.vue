<template>
  <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-200 hover:dark:bg-gray-700">
    <th
      scope="row"
      class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
    >
      {{ task.title }}
    </th>
    <td class="px-6 py-4">{{ task.description ? task.description : 'null' }}</td>
    <td class="px-6 py-4">{{ task.assigned_to ? task.assigned_to.username : 'null' }}</td>
    <td class="px-6 py-4">{{ task.created_by.user.username }}</td>
    <td class="px-6 py-4">{{ task.created_by.description ? task.created_by.description : 'null' }}</td>
  </tr>
</template>

<script>
export default {
  props: {
    task: {
      type: Object,
      required: true,
    },
  },
};
</script>
