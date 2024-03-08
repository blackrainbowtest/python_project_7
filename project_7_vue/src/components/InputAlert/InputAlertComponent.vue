<template>
  <div
    class="flex text-red-800 rounded-lg dark:text-red-400 select-none"
    role="alert"
  >
    <div class="absolute top-3 right-2">
      <svg
        aria-hidden="true"
        class="flex-shrink-0 w-5 h-5 cursor-pointer hover:dark:text-red-500"
        fill="currentColor"
        viewBox="0 0 20 20"
        xmlns="http://www.w3.org/2000/svg"
        @click="toggleError"
      >
        <path
          fill-rule="evenodd"
          d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
          clip-rule="evenodd"
        ></path>
      </svg>
    </div>
    <!-- <span class="sr-only">Info</span> -->
    <div v-show="showError" class="absolute left-0 text-sm font-medium">
      <span v-for="(message, idx) in errorMessage" :key="idx">
        {{ message?.length > 47 ? `${message.slice(0, 45)}...` : message }}
      </span>
      <span v-if="errorCount">
        Wait
        {{ sowTime(errorCount) }}
      </span>
    </div>
  </div>
</template>

<script>
import { mapMutations, mapGetters, mapActions } from "vuex";

export default {
  data() {
    return {
      showError: false,
      isTimer: false,
    };
  },
  props: {
    errorMessage: {
      type: Object,
    },
    errorCount: {
      type: Number,
    },
  },
  computed: {
    ...mapGetters({ getCountDown: "getCountDown" }),
  },
  methods: {
    ...mapMutations({ countDownTime: "countDownTime" }),
    ...mapActions({ countDownTimer: "countDownTimer" }),
    toggleError() {
      this.showError = !this.showError;
    },
    sowTime(value) {
      if (value) {
        let date = new Date(0);
        date.setSeconds(value);
        var timeString = date.toISOString().substring(11, 19);
        return timeString;
      }
    },
  },
  watch: {
    errorCount: {
      handler(value) {
        if (value > 0) {
          if(!this.isTimer) {
            this.isTimer = true
            setTimeout(() => {
              this.countDownTime();
              this.isTimer = false
            }, 1000);
          }
        } else if(value === 0) {
          this.showError = false
        }
      },
      immediate: true,
    },
  },
};
</script>
