module.exports = {
  extends: ["airbnb", "prettier"],

  rules: {
    // `.jsx` extension cannot be used with React Native
    // https://github.com/airbnb/javascript/issues/982
    "react/jsx-filename-extension": ["error", { extensions: [".js", ".jsx"] }],
    "arrow-body-style": 0
  }
};
