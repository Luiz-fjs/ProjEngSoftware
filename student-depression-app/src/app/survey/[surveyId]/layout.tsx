
export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <>
            <div className="fixed top-0 w-full backdrop-blur-md">
            </div>
            {children}
        </>
    )
}