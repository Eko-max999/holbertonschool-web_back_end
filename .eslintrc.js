module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    "airbnb-base",
    "plugin:jest/all"
  ],
  globals: {
    Atomics: "readonly",
    SharedArrayBuffer: "readonly",
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: "module",
  },
  plugins: ["jest"],
  rules: {
    "no-console": "off",
    "shadowed-variable": "off",
    "no-shadow": "off",
    "no-restricted-syntax": [
      "error",
      "LabeledStatement",
      "WithStatement"
    ]
  }
};
