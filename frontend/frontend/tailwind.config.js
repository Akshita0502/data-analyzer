/** @type {import("tailwindcss").Config} */ // helps understand tailwind configuration.
export default{  // expoort this configuration so tailwind reads it 
    content: [
        "./index.html",
       "./src/**/*.{js,jsx,ts,tsx}" // look inside the folder src, look inside all subfolders match with js jsx 
        // file matching system  known as glob pattern.
    ],
    theme: {
        extend: {},
    },
    plugins: []
}