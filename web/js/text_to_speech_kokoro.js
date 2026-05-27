import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Emiguru.KokoroTTS",
    async nodeCreated(node) {
        if (node.comfyClass === "Emiguru_KokoroTTS") {
            // Set seed widget to hidden input
            const seedWidget = node.widgets.find((w) => w.name === "seed");
            if (seedWidget) {
              seedWidget.type = "HIDDEN";
            }
        }
    }
});