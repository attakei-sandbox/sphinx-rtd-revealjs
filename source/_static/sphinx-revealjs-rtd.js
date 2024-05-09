window.RevealRTD = window.RevealRTD || {
  id: "RevealRTD",
  init(deck) {
    initRTD(deck);
  },
};

const initRTD = function (Reveal) {
  const config = Reveal.getConfig().readthedocs || undefined;
  if (!config) {
    return;
  }
  const container = document.createElement("div");
  container.id = "revealjs-readthedocs";

  container.innerHTML = config;
  document.querySelector(".reveal").appendChild( container );
}
