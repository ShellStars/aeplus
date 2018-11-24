<template>
  <div id="introduction">
    <p class="ask">
      <b>我们是谁？<br>参加我们的 Today at Apple 课程。</b>
    </p>
    <p class="introduce_me">
      Whether you’re building a design system or working with the
      company style guide, Libraries let you create, update and
      share a single source of truth for all your design components.
    </p>
  </div>
</template>

<script>
export default {
  name: 'introduction'
}
</script>

<style scoped>
  #introduction {
    height: 360px;
    background: url("/static/images/introduction_bg.png") no-repeat center 0;
    background-size: 120% 405px;
  }
  #introduction>.ask{
    color: #ffffff;
    margin: 0;
    padding-top: 120px;
    width: 504px;
    margin-left: auto;
    margin-right: auto;
  }
  #introduction>.ask>b {
    font-size: 1.8em;
    letter-spacing: 2px;
  }
  #introduction>.introduce_me{
    width: 560px;
    margin-left: auto;
    margin-right: auto;
    color: #888888;
    text-align: left;
    font-size: 1.1em;
  }
</style>
