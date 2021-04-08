import Image from 'next/image'

export default () => (
  <div class="container">
    <div class="absolute m-4 top-2 right-8">
      <button class="content-center bg-gray-200 font-mono text-gray-800 font-bold p-2 rounded" href="/">Connect Exchange</button>
    </div>
    <div class="flex m-auto content-center p-8">
      <a class="m-auto text-5xl font-bold font-sans text-yellow-200 cursor-pointer md:mb-0" href="/">Crypto.Holdings<span class="ml-2 font-mono text-xs opacity-50 text-gray-200">alpha</span></a>
    </div> 
    <div class="flex m-auto content-center">
      <h1 class="m-auto text-sm font-sans text-gray-200 md:mb-0" >Current Balance</h1>
    </div>
    <div class="flex m-auto content-center">
      <a class="m-auto text-6xl font-bold font-sans text-gray-200 md:mb-0" href="/">$ 20,023.23</a>
    </div>
    <div class="flex m-auto content-center p-10 left-20">
    <Image
        src="/../public/BTC.png"
        alt="Bitcoin"
        width={954}
        height={582}
      />
    </div>
    <div class="flex m-auto content-center p-10">
    <Image
        src="/../public/BNB.png"
        alt="Binance coin"
        width={454}
        height={282}
      />
      <br></br>
      <Image
        src="/../public/ETH.png"
        alt="Ether"
        width={454}
        height={282}
      />
    </div>             









  </div>
)
