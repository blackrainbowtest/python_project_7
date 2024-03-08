<template>
  <div class="sticky top-0">
    <nav class="bg-white border-gray-200 dark:bg-gray-900">
      <div
        class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4"
      >
        <router-link to="/" class="flex items-center">
          <img src="../../assets/coLogo.png" class="h-8 mr-3" alt="CO Logo" />
          <span
            class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white"
            >SaveToDoer</span
          >
        </router-link>
        <div class="dropdown flex items-center md:order-2">
          <!-- profile menu button -->
          <ButtonProfileComponent @toggleProfile-data="toggleProfile" />
          <!-- profile dropdown menu -->
          <ProfileDropdownComponent
            @defaultMode-data="defaultMode"
            @lightMode-data="lightMode"
            @darkMode-data="darkMode"
            @openModal-data="openModal"
            @logoutSuccess-data="logoutSuccess"
            @invite-data="invite"
            :showProfile="showProfile"
            :isUser="isUser"
            :profile="user"
          />
          <!-- mobile menu button -->
          <ButtonMobileComponent @toggleNav-data="toggleNav" />
        </div>
        <NavMenuListComponent :show-menu="showMenu" />
      </div>
    </nav>
  </div>
  <ModalComponent
    v-if="isModal"
    @closeModal-data="closeModal"
    @logIn-data="logIn"
    :isModal="isModal"
  />
  <ModalInvite :isInvite="isInvite" @closeInvite-data="closeInvite" />
  <ModalChangePassword  v-if="isPassword" :isPassword="isPassword" @closePassword-data="closeChangePassword"/>
  <router-view />
</template>
<script>
import ProfileDropdownComponent from "@/components/ProfileDropdown/ProfileDropdownComponent.vue";
import ButtonProfileComponent from "@/components/ButtonProfile/ButtonProfileComponent.vue";
import ButtonMobileComponent from "@/components/ButtonMobile/ButtonMobileComponent.vue";
import NavMenuListComponent from "@/components/NavMenuList/NavMenuListComponent.vue";
import ModalComponent from "@/components/Modal/ModalComponent.vue";
import ModalInvite from "@/components/Modal/ModalInvite.vue";
import ModalChangePassword from "../Modal/ModalChangePassword.vue";
import router from '@/router'

import { mapGetters, mapActions } from "vuex";

export default {
  data() {
    return {
      showMenu: false,
      showProfile: false,
      isModal: false,
      isInvite: false,
      isPassword: false,
      isUser: localStorage?.user ? true : false,
      theme: localStorage.theme === "dark" ? true : false,
      user: {},
    };
  },
  computed: {
    ...mapGetters({ getUser: "getUser" }),
  },
  components: {
    ProfileDropdownComponent,
    ButtonProfileComponent,
    ButtonMobileComponent,
    NavMenuListComponent,
    ModalComponent,
    ModalInvite,
    ModalChangePassword,
  },
  mounted() {
    this.checkMode();
    this.checkProfile();
    if(this.$route.query?.invite) {
      this.openModal()
    }
    if(this.$route.query?.shortcode) {
      // ---------------------------------------------
      this.openChangePassword()
      // ---------------------------------------------
    }
  },
  methods: {
    ...mapActions({ profile: "profile" }),
    toggleNav() {
      this.showMenu = !this.showMenu;
    },
    toggleProfile() {
      this.showProfile = !this.showProfile;
      document.addEventListener("mousedown", this.closeWhenClickedOutside);
    },
    closeWhenClickedOutside(event) {
      if (
        !event.target.closest(".dropdown") &&
        !event.target.closest(".profile")
      ) {
        this.showProfile = false;
        document.removeEventListener("mousedown", this.closeWhenClickedOutside);
      }
    },
    checkMode() {
      if (
        localStorage.theme === "dark" ||
        (!("theme" in localStorage) &&
          window.matchMedia("(prefers-color-scheme: dark)").matches)
      ) {
        document.documentElement.classList.add("dark");
      } else {
        document.documentElement.classList.remove("dark");
      }
    },
    lightMode() {
      localStorage.theme = "light";
      this.checkMode();
    },
    darkMode() {
      localStorage.theme = "dark";
      this.checkMode();
    },
    defaultMode() {
      localStorage.removeItem("theme");
      this.checkMode();
    },
    closeModal() {
      this.isModal = false;
      document.removeEventListener("mousedown", this.closeWhenClickedOutsideModal);
    },
    logIn() {
      this.isModal = false;
      document.removeEventListener("mousedown", this.closeWhenClickedOutsideModal);
      this.isUser = localStorage?.user ? true : false;
      this.profile();
      this.user = this.getUser;
    },
    openModal() {
      this.isModal = true;
      this.showProfile = false;
      document.removeEventListener("mousedown", this.closeWhenClickedOutside);
      document.addEventListener("mousedown", this.closeWhenClickedOutsideModal);
    },
    closeChangePassword() {
      this.isPassword = false
      document.removeEventListener("mousedown", this.closeWhenClickedOutsidePassword);
    },
    openChangePassword() {
      this.isPassword = true;
      this.showProfile = false;
      document.removeEventListener("mousedown", this.closeWhenClickedOutside);
      document.addEventListener("mousedown", this.closeWhenClickedOutsidePassword);
    },
    closeWhenClickedOutsidePassword(event) {
      if (
        !event.target.closest(".modal-body") &&
        !event.target.closest(".modal-button")
      ) {
        this.isPassword = false;
        document.removeEventListener(
          "mousedown",
          this.closeWhenClickedOutsidePassword
        );
        router.push('/')
      }
    },
    closeWhenClickedOutsideModal(event) {
      if (
        !event.target.closest(".modal-body") &&
        !event.target.closest(".modal-button")
      ) {
        this.isModal = false;
        document.removeEventListener(
          "mousedown",
          this.closeWhenClickedOutsideModal
        );
        router.push('/')
      }
    },
    checkProfile() {
      if (localStorage?.user) {
        this.profile();
        this.user = this.getUser;
      }
    },
    logoutSuccess() {
      this.toggleProfile();
      this.isUser = false;
    },
    invite() {
      this.toggleInvite();
    },
    closeInvite() {
      this.isInvite = false;
      document.removeEventListener("mousedown", this.closeWhenClickedOutsideInvite);
    },
    toggleInvite() {
      this.isInvite = !this.isInvite;
      document.addEventListener("mousedown", this.closeWhenClickedOutsideInvite);
    },
    closeWhenClickedOutsideInvite(event) {
      if (
        !event.target.closest(".modal-body") &&
        !event.target.closest(".modal-button") &&
        !event.target.closest(".profile-class")
      ) {
        this.isInvite = false;
        document.removeEventListener(
          "mousedown",
          this.closeWhenClickedOutsideInvite
        );
      }
    },
  },
};
</script>

<style scoped>
/* light theme */

/* animations */
/* *-enter */ /* *-leave */
/* *-enter-active */ /* *-leave-active */
/* *-enter-to */ /* *-leave-to */

.menu-enter-active,
.menu-leave-active {
  transition: all 0.5s;
}

.menu-enter,
.menu-leave-to {
  transform: translateX(50px);
}
</style>
